$uri = "https://app-deplyment-4.onrender.com"
$body = @{
    "minutes_played" = 1000  # Example value
    "highest_value" = 1000000 # Example value
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri $uri -Method Post -Body $body -ContentType "application/json"



curl -X POST "https://app-deplyment-4.onrender.com" \
     -H "Content-Type: application/json" \
     -d '{
        "minutes_played": 1000,
        "highest_value": 1000000
     }'