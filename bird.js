window.onload = async () => {
  const dataExists = localStorage.getItem("birds");
  let data = [];
  if (dataExists) {
    data = JSON.parse(dataExists);
  } else {
    const dataurl = "./birds.json";
    data = await fetch(dataurl)
      .then((response) => response.json());
  }
  localStorage.setItem('birds', JSON.stringify(data));

  document.getElementById("count").innerText = `${data.length} birds found.`;
};
