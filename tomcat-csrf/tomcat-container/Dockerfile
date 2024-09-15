# Usa un'immagine base con Maven e JDK
FROM maven:3.8.5-openjdk-11 AS builder

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file pom.xml e le altre dipendenze
COPY dummy-app/pom.xml .

# Prepara le dipendenze
RUN mvn dependency:go-offline

# Copia il resto dell'app e builda
COPY dummy-app/ .
RUN mvn clean package

# Inizia a costruire l'immagine di Tomcat
FROM tomcat:7.0.59

EXPOSE 8080

# Copia il file WAR generato nella directory webapps di Tomcat
COPY --from=builder /app/target/*.war /usr/local/tomcat/webapps/simple-app-1.0-SNAPSHOT.war

# Copia i file di configurazione
COPY web.xml /usr/local/tomcat/conf/web.xml
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
