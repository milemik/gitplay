const assert = require("assert");
const { addUser } = require("../index");


describe("addUser", () => {
    beforeEach(() => {
        document.body.innerHTML = `
        <div class="wrapper">
            <h1>GitPlay</h1>
            <h5>Hello World</h5>
            <p id="message"></p>
            <p id="hello"></p>
            <p>By Mile</p>
        </div>
        `;
    });
    test("test document", () => {
        assert.deepStrictEqual(document.getElementById("message").textContent, "");
    })
    test("add user", () => {
        let res = addUser();
        assert.deepStrictEqual(res, "OK");
    });
});
