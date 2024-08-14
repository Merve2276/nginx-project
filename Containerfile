# Nginx'in resmi imajını kullan
FROM nginx:latest

# Nginx'in çalışacağı portu belirt
EXPOSE 80

# Nginx'i başlat
CMD ["nginx", "-g", "daemon off;"]

