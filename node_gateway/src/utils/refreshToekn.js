const RefreshToken = require("./models/refreshToken");

const createRefreshToken = async (userId, tokenValue ,expiresInDays) => {
  //const expiresInDays = 7; // e.g. token valid for 7 days
  const expiresAt = new Date(Date.now() + expiresInDays * 24 * 60 * 60 * 1000);

  const refreshToken = new RefreshToken({
    token: tokenValue,
    userId,
    expiresAt
  });

  await refreshToken.save();
  return refreshToken;
};

module.exports = createRefreshToken;