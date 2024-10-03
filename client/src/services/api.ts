import axios from "axios";
import { ArtPiece, Review } from "../types";
import { store } from "../store";

const API_URL = import.meta.env.SERVER_URL;

const axiosInstance = axios.create({
  baseURL: API_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const token = store.getState().auth.token;
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const getArtPieces = async (
  page: number = 1,
  limit: number = 20
): Promise<ArtPiece[]> => {
  const response = await axiosInstance.get(
    `/art-pieces/?skip=${(page - 1) * limit}&limit=${limit}`
  );
  return response.data;
};

export const getArtPiece = async (id: number): Promise<ArtPiece> => {
  const response = await axiosInstance.get(`${API_URL}/art-pieces/${id}`);
  return response.data;
};

export const getReviews = async (artPieceId: number): Promise<Review[]> => {
  const response = await axiosInstance.get(`${API_URL}/reviews/${artPieceId}`);
  return response.data;
};

export const login = async (username: string, password: string) => {
  const response = await axiosInstance.post(`/users/token`, {
    username,
    password,
  });
  return response.data;
};

export const register = async (
  username: string,
  email: string,
  password: string
) => {
  const response = await axiosInstance.post(`/users/register`, {
    username,
    email,
    password,
  });
  return response.data;
};
