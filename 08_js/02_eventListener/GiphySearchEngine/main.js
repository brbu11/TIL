/* 1. <input> 태그 안의 값을 잡는다. */


/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */


/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */

//AJAX 요청을 보낸다
/*
 기존요청:
 1. 링크누른다
 2. href 로 요청간다.
 3. 브라우저가 새로고침되고 응답을 render한다.
 */

/*
AJAX 요청:
1. 어떤 event가 발생한다.
2. 요청을 전송하고, 응답이 도착 할 때까지 기다린다. 화면 전환은 없다.
3. 응답이 오면, 지금 문서에서 응답내용을 추가로 render 한다.
 */
/*
기존의 요청
 */
const inputArea = document.querySelector('#js-userinput');
const button = document.querySelector('#js-go');
const resultArea = document.querySelector('#result-area');

inputArea.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
        searchAndPush(inputArea.value);
    }
});
button.addEventListener('click', e => {
    searchAndPush(inputArea.value);
});

const searchAndPush = keyword => {
    const KEY = 'VdcXw7tsdue4Jun0mV5v42btUgcw8drf';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;
    const AJAXCall = new XMLHttpRequest();
    AJAXCall.open('GET', URL);
    AJAXCall.send();
    AJAXCall.addEventListener('load', e => {
        const parseData = JSON.parse(e.target.response);
        pushToDOM(parseData);
    });
    const pushToDOM = dataset => {
        resultArea.innerHTML = null;
        const dataArray = dataset.data;
        let imgUrl;
        let element;
        for (const imgData of dataArray) {
            imgUrl = (imgData.images.fixed_height.url);
            element = document.createElement('img');
            element.classList.add('container-image');
            element.src = imgUrl;
            resultArea.appendChild(element);
        }
    };
};

