FROM openjdk:17-jdk-alpine
ADD . .
RUN ./mvnw clean package
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]