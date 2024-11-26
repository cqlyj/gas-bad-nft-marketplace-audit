/*
 * Certora Formal Verification Spec for GasBadNftMarketplace
 *
 * This spec is technically unsound because we make summaries about the functions, and are using optimistic fallback
 */ 

// certoraRun ./certora/conf/GasBad.conf --optimistic_fallback

methods {
    function _.safeTransferFrom(address, address, uint256) external => DISPATCHER(true);
    function _.onERC721Received(address, address, uint256, bytes) external => DISPATCHER(true); 
}

ghost mathint listingUpdatesCount {
    // initial state will be 0
    // require this to be true
    init_state axiom listingUpdatesCount == 0;
}
ghost mathint log4Count {
    init_state axiom log4Count == 0;
}

hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price {
    listingUpdatesCount = listingUpdatesCount + 1;
}

hook LOG4(uint offset, uint length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4) {
    log4Count = log4Count + 1;
}

/*//////////////////////////////////////////////////////////////
                             RULES
//////////////////////////////////////////////////////////////*/

invariant anytime_mapping_updated_emit_event()
    listingUpdatesCount <= log4Count;