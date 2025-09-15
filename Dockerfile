FROM ubuntu:22.04
WORKDIR /app
COPY wisecow.sh .
RUN apt-get update && \
    apt install fortune-mod cowsay netcat-openbsd -y && \
    chmod +x wisecow.sh && \
    rm -rf /var/lib/apt/lists/*
    
ENV PATH="/usr/games:$PATH"

EXPOSE 4499

CMD ["./wisecow.sh"]