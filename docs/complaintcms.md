### tailwindcss 
```
mkdir frontend
npm install -D tailwindcss postcss autoprefixer postcss-cli
npx tailwindcss init -p
```
package.json
```
{
  "devDependencies": {
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.5",
    "postcss-cli": "^9.1.0",
    "tailwindcss": "^3.0.7"
  },
  "scripts": {
    "build": "postcss css/tailwind.css -o ../complaintcms/static/complaintcms/css/main.css"
  }
}
```
postcss.config.js
```
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```
taiwind.config.js
```
module.exports = {
  content: [
    "../complaintcms/static/complaintcms/**/*.{html,js}",
    "../complaintcms/**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```
引入tailwindcss
```
mkdir css
cd css
touch tailwind.css
```
frontend/css/tailwind.css
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

forms
```
npm install @tailwindcss/forms
```