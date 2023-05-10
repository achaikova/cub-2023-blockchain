## Publishing Poetry Text in Ethereum Blockchain

### Project Setup

1. Install the required dependencies using npm:
```
npm init --yes
npm install --save-dev hardhat  
npm install --save-dev @openzeppelin/contracts
npm install --save-dev @nomiclabs/hardhat-ethers "ethers@^5.0.0"
```

2. Create a `.env` file in the root folder and add your Alchemy API key and wallet private key - `API_URL` and `PRIVATE_KEY`.

### Deploying the Smart Contract

1. Compile the smart contract:

   ```
   npx hardhat compile
   ```

2. Deploy the smart contract to the Ethereum network:

   ```
   npx hardhat run scripts/deploy.js --network <your-preferred-network>
   ```

   Replace `<your-preferred-network>` with the desired Ethereum network (e.g., goerli, sepolia).

3. Once the deployment is successful, you will see a contract address (e.g., 0x1234abcd...).

4. Add contract address to the `.env` file (`CONTRACT_ADDRESS`)

### Publishing Poetry

Publish a poem and create an associated NFT by running the following command:

```
npx hardhat publish --poem "Your poem text goes here"
```

Replace `Your poem text goes here` with the text of your poem.

