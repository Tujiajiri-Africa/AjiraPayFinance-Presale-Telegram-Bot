v2_abi = [{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address payable","name":"_treasury","type":"address"},{"internalType":"uint256","name":"_durationInDays","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor", "name":""},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"beneficiary","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenAmountReceived","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"address","name":"destination","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"ClaimUnsoldTokens","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"ClosePresale","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"CloseTokenClaims","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"beneficiary","type":"address"},{"indexed":True,"internalType":"uint256","name":"weiAmount","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"tokenAmountBought","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Contribute","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"OpenPublicSale","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"OpenTokenClaims","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"PausePresale","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"address","name":"destinationWallet","type":"address"},{"indexed":True,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"RecoverBNB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"address","name":"destination","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"RecoverERC20Tokens","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"StartPresale","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"UnpausePresale","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":False,"internalType":"uint256","name":"prevCap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newCap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"UpdateMaxCap","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"UpdatePrivateSalePrice","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"caller","type":"address"},{"indexed":True,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"UpdatePublisSalePrice","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MANAGER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"activatePhase1","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"activatePhase2","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"activatePhase3","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"ajiraPayFinanceToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"canClaimTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimContribution","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimUnsoldTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contribute","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getContractBNBBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContractTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"investors","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isActiveInvestor","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOpenForClaims","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPhase1Active","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPhase2Active","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPhase3Active","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPresaleOpen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPresalePaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastUserBuyTimeInSec","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPossibleInvestmentInWei","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTokenCapForPresale","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTokensToPurchasePerWallet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nextPossiblePurchaseTimeByUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase1PricePerTokenInWei","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase1TotalTokensToSell","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase2PricePerTokenInWei","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase2TotalTokensToSell","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase3PricePerTokenInWei","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phase3TotalTokensToSell","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"presaleDurationInSec","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"recoverBNB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"recoverLostTokensForInvestor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setPhase1PriceInWei","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setPhase2PriceInWei","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setPhase3PriceInWei","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_status","type":"bool"}],"name":"setPresaleClaimsStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_days","type":"uint256"}],"name":"setPresaleDurationInDays","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_status","type":"bool"}],"name":"setPresalePauseStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_status","type":"bool"}],"name":"setPresaleProgressStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalBNBInvestmentsByIUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalInvestors","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalTokenInvestmentPhase1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalTokenInvestmentPhase2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalTokenInvestmentPhase3","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalWeiInvestmentPhase1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalWeiInvestmentPhase2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalPersonalWeiInvestmentPhase3","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalTokenContributionsByUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"totalTokenContributionsClaimedByUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensClaimed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensSold","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensSoldInPhase1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensSoldInPhase2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensSoldInPhase3","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalWeiRaised","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalWeiRaisedInPhase1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalWeiRaisedInPhase2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalWeiRaisedInPhase3","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"updateMaxTokenCapForPresale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_phase1Amount","type":"uint256"},{"internalType":"uint256","name":"_phase2Amount","type":"uint256"},{"internalType":"uint256","name":"_phase3Amount","type":"uint256"}],"name":"updatePresalePhaseAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_newTreasury","type":"address"}],"name":"updateTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive", "name":""}]