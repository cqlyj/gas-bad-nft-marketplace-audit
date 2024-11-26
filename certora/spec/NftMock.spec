/*
 * Certora Formal Verification Spec for NftMock
 */ 

// certoraRun ./certora/conf/NftMock.conf 

methods {
    function totalSupply() external returns uint256 envfree;
    function mint() external;
    function balanceOf(address) external returns uint256 envfree;
}

// rule sanity {
//     satisfy true;
// }

// invariant totalSupplyIsNotNegative()
//     totalSupply() >= 0;

rule mintingMintsOneNft() {
    env e;
    address minter;

    require e.msg.value == 0;
    require e.msg.sender == minter;

    mathint balanceBefore = balanceOf(minter);

    currentContract.mint(e);

    assert to_mathint(balanceOf(minter)) == balanceBefore + 1, "Only one NFT should be minted";
}

// This will fail, just to show the parametric function
rule noChangeToTotalSupply(method f) {
    uint256 totalSupplyBefore = totalSupply();

    env e;
    calldataarg arg;
    f(e, arg);

    assert totalSupply() == totalSupplyBefore, "Total supply should not change";
}