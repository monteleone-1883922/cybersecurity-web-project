FROM tomcat:7.0.56


# Copia i file di configurazione necessari per attivare le applicazioni Manager e Host Manager
COPY tomcat-users.xml /usr/local/tomcat/conf/

# Espone le porte per l'accesso al Manager
EXPOSE 8080

# Copia il file WAR nella directory webapps di Tomcat
COPY dummy-app/target/simple-app-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/

COPY web.xml /usr/local/tomcat/conf/web.xml

