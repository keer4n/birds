window.onload = async () => {
  console.log("executing");
  const dataExists = localStorage.getItem("birds");
  let data = [];
  if (dataExists) {
    data = JSON.parse(dataExists);
  } else {
    const dataurl = "./birds.json";
    data = await fetch(dataurl)
      .then((response) => response.json())
      .catch((e) => console.error);
    console.log("birds", data);
  }
  localStorage.setItem("birds", JSON.stringify(data));

  document.getElementById("count").innerText = `${data.length} birds found.`;
};
