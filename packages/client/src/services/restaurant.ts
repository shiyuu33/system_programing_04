import { mockResponseData } from "@/mocks/resutaurant"
export class Restaurant {
    url: string
    constructor() {
        this.url = import.meta.env.VITE_API_URL
    }
    async getRestaurantsShopList(query: {[key: string]: string} = {}): Promise<unknown> {
        try {
            const responses = await {...mockResponseData}
            if(responses.message !== "ok") {
                throw new Error("Error is occurred")
            }
            return responses.data.results.shop
        } catch(e) {
            console.error(e)
        }
    }
}