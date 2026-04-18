# stage 1 build
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./

RUN npm install --only=production --no-cache
COPY . .

# STAGE 2 PRODUCTION RUNTIME
FROM node:20-alpine

RUN addgroup -g 1001 -S nodejs && \
    adduser -S -u 1001 -G nodejs nodejs

WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app .
USER nodejs
EXPOSE 3000
ENV NODE_ENV=production

CMD ["npm", "start"]