import axios from "axios";
import { BASE_URL } from "./apiConfig";

const ApiService = {
    baseURL: BASE_URL,
    
    async get(url) {
        try {
            const response = await axios.get(`${this.baseURL}${url}`)
            return response.data
        } catch (error) {
            throw new Error("An error ocurred during API request: ", error.message);
        }
    }
}

export default ApiService;