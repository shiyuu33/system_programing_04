export class Restaurant {
    url: string
    constructor() {
        this.url = import.meta.env.VITE_API_URL
    }
    async getRestaurantsShopList(query: {[key: string]: string} = {}): Promise<unknown> {
        try {
            const responses = await fetch(`${this.url}/api/restaurants?start_place=${query.startPlace}&end_place=${query.endPlace}`)
            if(!responses.ok) {
                throw new Error("Error is occurred")
            }
            const json = await responses.json();
            return json.data.results.shop
        } catch(e) {
            console.error(e)
        }
    }
}