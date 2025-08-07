 const themes = {
    light: {
      "--bg-color": "white",
      "--text-color": "black",
      "--link-color": "blue",
      "--bg-image": "none"
    },
    dark: {
      "--bg-color": "#121212",
      "--text-color": "#f0f0f0",
      "--link-color": "#90caf9",
      "--bg-image": "none"
    },
    halloween: {
      "--bg-color": "#000000",
      "--text-color": "#FFA500",
      "--link-color": "#FF4500",
      "--bg-image": "url('/static/images/important.gif')"
    }
  };

  function setTheme(theme) {
    const root = document.documentElement;
    const settings = themes[theme];
    for (const key in settings) {
      root.style.setProperty(key, settings[key]);
    }
    localStorage.setItem("theme", theme);
  }

  // Load saved theme on page load
  const savedTheme = localStorage.getItem("theme") || "light";
  setTheme(savedTheme);
