# Semantic Music Search According to Lyrics

<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
![](demo.gif)
<br />
<div align="center">
  <h3 align="center">music-search</h3>
  <p align="center">
    Semantic search engine for finding your favourite music according to the lyrics!
    <br />
    <a href="https://search-frontend.fly.dev"><strong>Try it now »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#Features">Features</a></li>
      </ul>
    </li>
    <li><a href="#payloads-and-encoded-vectors">Payloads and Encoded Vectors</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The music search app is essentially a semantic search engine based on a sentence transformer, <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2">"all-MiniLM-L12-v2"</a> model and powered by <a href="https://cloud.qdrant.io">Qdrant Vector Search Cloud</a>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

all-MiniLM-L12-v2 model has been trained on a large and diverse dataset of over 1 billion training pairs,and tuned for many use-cases. 

The dataset used in this project is an English subset of <a href="https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres">Song lyrics from 79 musical genres</a> I specifically created for searching within English lyrics, which contains 191,814 instances of lyrics with their corresponding artists and song names.

The front-end was developed with Vue.js framework and deployed on fly.io. The back-end was developed with FastAPI and uvicorn and deployed on fly.io.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features

* Search music according to lyrics, optionally narrow down the results on the artist name
* Look for music matches text which descibes feelings, weathers etc.
* Search similiar songs based on the previous search result

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Payloads and Encoded Vectors

<a href="https://drive.google.com/drive/folders/1tH-PfI24Ov8tFu6O1gu8NKKd0DE4knlT?usp=share_link">Google Drive Folder</a> 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add search filter "artist"
- [x] Add read-more button on the lyrics card
- [ ] Add back to homepage button from search results page
- [ ] Add Spotify links to the search results
- [ ] Improve performance with larger models
- [ ] Add more search filters
- [ ] Multi-language Support
    - [x] English
    - [ ] Portuguese

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tianxiang Wang  - tianxiang.wang@nixtasy.com

Project Link: [https://github.com/nixtasy/music-search/](https://github.com/nixtasy/music-search/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I've included a few tools,products and articles which inspired the projects:

* [Material Design for Bootstrap 5 & Vue 3](https://mdbootstrap.com/docs/vue/)
* [Qdrant vector similarity search engine](https://qdrant.tech)
* [How to Create a web app ..for generating and showcasing images ...](https://medium.com/@sangeeth123sj/how-to-create-a-web-app-using-fastapi-vuejs-and-mongodb-for-generating-and-showcasing-images-193ccdb20091)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/nixtasy/music-search/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tianxiangwang/
