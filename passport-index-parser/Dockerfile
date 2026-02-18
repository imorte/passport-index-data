FROM golang:1.26-alpine AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY *.go ./
RUN CGO_ENABLED=0 go build -o /passport-index-parser .

FROM alpine:3.21
RUN apk add --no-cache ca-certificates
COPY --from=build /passport-index-parser /usr/local/bin/passport-index-parser
WORKDIR /data
ENTRYPOINT ["passport-index-parser"]
