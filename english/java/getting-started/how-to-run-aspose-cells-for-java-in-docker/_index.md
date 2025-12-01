---
title: How to Run Aspose.Cells for Java in Docker
type: docs
description: "Run Aspose.Cells for Java in a Docker container for Linux. "
weight: 139
url: /java/how-to-run-aspose-cells-in-docker/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Microservices, in conjunction with containerization make it possible to easily combine technologies. Docker allows you to easily integrate Aspose.Cells functionality into your application, regardless of what technology is in your development stack.

In case you are targeting microservices, or if the main technology in your stack is not .NET, C++ or Java, but you need Aspose.Cells functionality, or if you already use Docker in your stack, then you may be interested in utilizing Aspose.Cells for Java in a Docker container.

## Prerequisites

- Docker must be installed on your system. 

## Create a Java Application

In this example, you create a Java application that makes a simple xlsx file, saves it and reads it. The application can then be built and run in Docker.

### Creating the Java Application

Create the Java Application in Eclipse using the following code. In this example, we use Aspose.Cells for Java creates a new xlsx worksheet and sets its sheet name and cell values, then reads them and outputs them.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Make the Java Application into a jar package

The following figure shows a way to make a jar package using "Export" menu in Eclipse.

**![Make Jar using Eclipse](MakeJar.png)**

Now that we wrote a Java program using Aspose.Cells for Java, we got a jar package. Next we'll make a dockerfile.

### Configuring a Dockerfile

The next step is to create and configure the Dockerfile.

1. Create the Dockerfile and place it next to the jar package. Keep this file name without extension (the default).
2. In the Dockerfile, specify:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Building and Running the Application in Docker

Now the application can be built and run in Docker. Open your favorite command prompt, change directory to the folder with the Dockerfile and run the following command:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

After executing the above command, you will get the output of the XLSX worksheet and the result of the command line. At this point, a Java program has been successfully run in Linux Docker.
{{< app/cells/assistant language="java" >}}
