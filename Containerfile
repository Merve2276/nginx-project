# Nginx'in resmi imajını kullan
FROM nginx:latest

# Nginx'in çalışacağı portu belirt
EXPOSE 80

# Nginx'i başlat
CMD ["nginx", "-g", "daemon off;"]

# Nginx'in yapılandırma dosyasını kopyala
COPY nginx.conf /etc/nginx/nginx.conf

# Nginx'in yapılandırma dosyasını kopyala
COPY nginx.conf /etc/nginx/nginx.conf

# Statik içerikleri kopyala
COPY ./html /usr/share/nginx/html

