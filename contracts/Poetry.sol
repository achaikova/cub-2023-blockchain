// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PoetryPublisher is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    mapping(uint256 => string) private _poetryText;

    constructor() ERC721("PoetryToken", "POETRY") {}

     function publish(string memory poetry, string memory tokenURI) public returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _safeMint(msg.sender, newItemId);
        _poetryText[newItemId] = poetry;
        _setTokenURI(newItemId, tokenURI); // Set the tokenURI for the new token

        return newItemId;
    }


    function getPoetry(uint256 tokenId) public view returns (string memory) {
        require(
            _exists(tokenId),
            "PoetryPublisher: Query for nonexistent token"
        );

        return _poetryText[tokenId];
    }
}