# music-search

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
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/nixtasy/music-search/demo.gif" alt="Logo" width="80" height="80">
  </a>

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
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The music search app is essentially a semantic search engine based on a sentence transformer, <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2">"all-MiniLM-L12-v2"</a> model and powered by Qdrant vector search engine with a cloud solution.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The dataset used in this project is a English subset of <a href="https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres">Song lyrics from 79 musical genres</a> which contains 191,814 instances of lyrics with its corresponding artist and song name.

The front-end was developed with Vue.js framework and deployed on fly.io. The back-end was developed with FastAPI and uvicorn and deployed on fly.io.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features

* Search music according to lyrics, optionally narrow down the results on the artist name
* Look for music matches text which descibes feelings, weathers etc.
* Search similiar songs based on the previous search result

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add search filter "artist"
- [x] Add read-more button on the lyrics card
- [ ] Add back to homepage button from search results page
- [ ] Add Spotify links to the search results
- [ ] Multi-language Support
    - [x] English
    - [ ] Portuguese

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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

I've included a few of my favorites to kick things off!

* [Material Design for Bootstrap 5 & Vue 3](https://mdbootstrap.com/docs/vue/)
* [Qdrant vector similarity search engine](https://qdrant.tech)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/nixtasy/music-search/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tianxiangwang/
