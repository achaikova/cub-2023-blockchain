/** @type import('hardhat/config').HardhatUserConfig */

require('dotenv').config();
require("@nomiclabs/hardhat-ethers");

const { API_URL, PRIVATE_KEY, CONTRACT_ADDRESS } = process.env;

module.exports = {
  solidity: "0.8.18",
  defaultNetwork: "goerli",
  networks: {
    hardhat: {},
    goerli: {
      url: API_URL,
      accounts: [`0x${PRIVATE_KEY}`]
    },
  },
}

task("publish", "Publish a poem and create a NFT")
  .addParam("poem", "The text of the poem")
  .setAction(async (taskArgs, hre) => {
    const publishPoetry = async (poem) => {
      const accounts = await hre.ethers.getSigners();
      const poetryPublisherContract = await hre.ethers.getContractAt(
        "PoetryPublisher",
         CONTRACT_ADDRESS
      );

      const result = await poetryPublisherContract
        .connect(accounts[0])
        .publish(poem, { gasLimit: 300000 });
      return result.tokenId;
    };

    const tokenId = await publishPoetry(taskArgs.poem);
    console.log("Published poem with tokenId:", tokenId.toString());
  });
