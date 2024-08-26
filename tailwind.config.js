const { plugin } = require("postcss");

module.exports = {
    content: ['./tailwindcss.html', '/src/**/*.{js, ts, jsx, tsx}']
    theme: {
        extend: {},
    },
    plugins: [],
};