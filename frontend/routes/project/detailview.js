const express = require("express");
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.get("/api/project/detail", async (req, res) => {
  const { access } = req.cookies;

  try {
    const apiRes = await fetch(
      `${process.env.API_URL}/api/project/${req.params.slug}`,
      {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      }
    );

    const data = await apiRes.json();

    return res.status(apiRes.status).json(data);
  } catch (err) {
    return res.status(500).json({
      error: "Something went wrong when trying to retrieve the project",
    });
  }
});

module.exports = router;
