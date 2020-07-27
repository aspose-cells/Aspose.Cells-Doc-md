+++
title = "Setup and Installation Guidelines" 
description = "" 
weight = 20028 
+++

Aspose.Cells for Java : Setup and Installation Guidelines  

# Aspose.Cells for Java : Setup and Installation Guidelines


  

{{< panel title="Contents Summary" style="primary" >}}
*   1 [System Requirements](#SetupandInstallationGuidelines-SystemRequirements)
*   2 [Installation and Usage](#SetupandInstallationGuidelines-InstallationandUsage)
    *   2.1 [Linux:](#SetupandInstallationGuidelines-Linux:)
    *   2.2 [Windows:](#SetupandInstallationGuidelines-Windows:)
    *   2.3 [Mac:](#SetupandInstallationGuidelines-Mac:)
{{< /panel >}}
 

 

## System Requirements

Aspose.Cells for PHP via Java is platform independent API and can be used on any platform (Windows, Linux, MacOS etc.) where [PHP](http://www.php.net/downloads.php) 7 or greater versions is installed. The machine must have Oracle JDK 7 or greater versions before setting up the installation.

## Installation and Usage

Aspose.Cells for PHP via Java is distributed as a ZIP archive.

To setup environment, install and use Aspose.Cells for PHP via Java, follow the instructions:

### Linux:

*   Download [PHP](http://www.php.net/downloads.php) source and  install it. Or, use “sudo apt install php-xxx” command to install php binary.
*   Install Oracle JDK (1.7 or 1.8) for Linux, configure JAVA\_HOME environment variable.
*   Download/Get "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
*   Run “PHP/Java Bridge” in the above folder with below command.

$JAVA\_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET\_LOCAL:8080 >/dev/null 2>&1 &

*   Run "example.php" in “aspose.cells” folder to run the example with below command:

$ php example.php

### Windows:

*   Download [PHP](http://php.net/downloads.php) windows binary and add "php.exe" to PATH.
*   Install Oracle JDK (1.7 or 1.8) for Windows and configure JAVA\_HOME environment variable.
*   Download "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
*   Run “PHP/Java Bridge” in the above folder with below command. Select 8080 http listener port when the bridge started and click OK button.

\> %JAVA\_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar

*   Run "example.php" in “aspose.cells” folder to run the example with below command:

\> php example.php

### Mac:

*   Install [PHP](http://www.php.net/downloads.php).
*   Install Oracle JDK (1.7 or 1.8) for Mac, configure JAVA\_HOME environment variable.
*   Download "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
*   Run “PHP/Java Bridge” in the above folder with below command. Select 8080 http listener port when the bridge started and click OK button.

$ $JAVA\_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar

*   Run "example.php" in “aspose.cells” folder to run the example with below command:

$ php example.php

