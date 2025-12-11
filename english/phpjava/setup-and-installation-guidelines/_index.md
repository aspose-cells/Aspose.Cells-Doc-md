---
title: Setup and Installation Guidelines
type: docs
weight: 20
url: /php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "Setup Aspose.Cells for PHP via Java and installation guidelines."
ai_search_scope: cells_phpjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---



## **System Requirements**
Aspose.Cells for PHP via Java is a platform‑independent API and can be used on any platform (Windows, Linux, macOS, etc.) where PHP 7 or later is installed. The machine must have Oracle JDK 7 or later before setting up the installation.

## **Installation and Usage**
Aspose.Cells for PHP via Java is distributed as a ZIP archive.

To set up the environment, install, and use Aspose.Cells for PHP via Java, follow the instructions:

### **Linux:**
- Download the PHP source and install it, or use the `sudo apt install php-xxx` command to install the PHP binary.  
- Install Oracle JDK 7 or 8 for Linux and configure the `JAVA_HOME` environment variable.  
- Download the “Aspose.Cells for PHP via Java” API and extract it. A folder named `aspose.cells` will be created.  
- Download the PHP/Java Bridge binary (`JavaBridge.jar`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Download the Java.inc PHP library (`Java.inc`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Run the PHP/Java Bridge in the above folder using the following command:

| `$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &` |
|---|

- Run `example.php` in the `aspose.cells` folder using the following command:

| `$ php example.php` |
|---|

### **Windows:**
- Download the PHP Windows binary and add `php.exe` to the `PATH`.  
- Install Oracle JDK 7 or 8 for Windows and configure the `JAVA_HOME` environment variable.  
- Download the “Aspose.Cells for PHP via Java” API and extract it. A folder named `aspose.cells` will be created.  
- Download the PHP/Java Bridge binary (`JavaBridge.jar`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Download the Java.inc PHP library (`Java.inc`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Run the PHP/Java Bridge in the above folder using the following command. Select the 8080 HTTP listener port when the bridge starts and click the **OK** button:

| `%JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar` |
|---|

- Run `example.php` in the `aspose.cells` folder using the following command:

| `php example.php` |
|---|

### **Mac:**
- Install PHP.  
- Install Oracle JDK 7 or 8 for macOS and configure the `JAVA_HOME` environment variable.  
- Download the “Aspose.Cells for PHP via Java” API and extract it. A folder named `aspose.cells` will be created.  
- Download the PHP/Java Bridge binary (`JavaBridge.jar`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Download the Java.inc PHP library (`Java.inc`) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into the `aspose.cells` folder.  
- Run the PHP/Java Bridge in the above folder using the following command. Select the 8080 HTTP listener port when the bridge starts and click the **OK** button:

| `$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar` |
|---|

- Run `example.php` in the `aspose.cells` folder using the following command:

| `$ php example.php` |
|---|
