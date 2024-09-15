FROM tomcat:7.0.59

# make privilledged context
RUN sed -i 's/<Context>/<Context privileged="true">/' /usr/local/tomcat/conf/context.xml


#enable ssi
COPY web.xml /usr/local/tomcat/conf/web.xml

# create file printenv.shtml containing the vulnerable code
RUN mkdir -p /usr/local/tomcat/webapps/ROOT/ssi
COPY printenv.shtml /usr/local/tomcat/webapps/ROOT/ssi/printenv.shtml

CMD ["catalina.sh", "run"]
