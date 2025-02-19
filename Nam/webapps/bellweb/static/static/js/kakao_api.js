function getUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            console.log("서울시:", latitude, longitude);
            searchNearbyRestaurants(latitude, longitude);
        }, error => {
            console.error("위치 정보를 가져올 수 없습니다.", error);
        });
    } else {
        alert("이 브라우저에서는 위치 정보를 지원하지 않습니다.");
    }
}

