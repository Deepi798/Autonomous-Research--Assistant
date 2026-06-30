export const fetchResearch = async (topic) => {

  const response = await fetch(
    `http://127.0.0.1:8000/research?topic=${topic}`
  );

  return response.json();
};