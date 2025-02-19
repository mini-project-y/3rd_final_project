async function searchNearbyRestaurants(lat, lng) {
    const query = "한식"; // 한식 맛집 검색
    const url = `/kakao-api?query=${query}&x=${lng}&y=${lat}&radius=2000`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error("검색 실패:", error);
    }
}


function displayResults(data) {
    const mapContainer = document.getElementById('map');
    const mapOption = {
        center: new kakao.maps.LatLng(data[0].y, data[0].x),
        level: 5
    };
    const map = new kakao.maps.Map(mapContainer, mapOption);

    data.forEach(place => {
        const marker = new kakao.maps.Marker({
            position: new kakao.maps.LatLng(place.y, place.x),
            map: map
        });

        const infowindow = new kakao.maps.InfoWindow({
            content: `<div>${place.place_name}</div>`
        });

        kakao.maps.event.addListener(marker, 'click', () => {
            infowindow.open(map, marker);
        });
    });
}
