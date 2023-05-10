async function main() {
   const PoetryPublisher = await ethers.getContractFactory("PoetryPublisher");

   // Start deployment, returning a promise that resolves to a contract object
   const poetry_publisher = await PoetryPublisher.deploy();   
   
   console.log("Contract deployed to address:", poetry_publisher.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });