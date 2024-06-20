---
title: Загрузите и настройте Aspose.Cells в PHP
type: docs
weight: 10
url: /ru/java/download-and-configure-aspose-cells-in-php/
---

## **Загрузить необходимые библиотеки**
Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения примеров Aspose.Cells Java для PHP.

- **Aspose:** [Компонент Aspose.Cells for Java](https://downloads.aspose.com/cells/java/)
- [PHP/Java Bridge](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Загрузить примеры из сайтов социального кодирования**
Следующие версии выполняемых примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

-----
### **GitHub**
- **Aspose.Cells Java для примеров PHP** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Как настроить исходный код на платформе Linux**
Пожалуйста, следуйте этим простым шагам для открытия и расширения исходного кода при использовании:
## **1. Установите Tomcat Server**
Чтобы установить сервер Tomcat, выполните следующую команду в консоли Linux. Это успешно установит сервер Tomcat. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Загрузите и настройте PHP/JavaBridge**
Для загрузки бинарных файлов PHP/JavaBridge введите следующую команду в консоли Linux. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Разархивируйте бинарные файлы PHP/JavaBridge, выполнив следующую команду в консоли Linux. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Это извлечет файл **JavaBridge.war**. Скопируйте его в папку tomcat88 **webapps**, выполнив следующую команду в консоли Linux. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Если появляется сообщение об ошибке, установите **FastCGI**, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Настройка примеров Aspose.Cells Java для PHP**
Склонируйте примеры PHP, выполнив следующие команды в папке webapps/JavaBridge.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Как настроить исходный код на платформе Windows**
Пожалуйста, следуйте простым шагам ниже, чтобы настроить PHP/Java Bridge на платформе Windows

\1. Установите PHP5 и настройте его, как обычно.
\2. Установите JRE 6 (Java Runtime Environment), если у вас его еще нет. Вы можете проверить это в C:\Program Files и т. д. Вы можете загрузить его здесь. Я использую JRE 6, т.к. он совместим с PHP Java Bridge (PJB).

\3. Установите Apache Tomcat 8.0. Вы можете загрузить его здесь.

4. Загрузите [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Скопируйте этот файл в директорию веб-приложений tomcat.
(например, C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

\5. Перезапустите службу Apache tomcat.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Скопируйте ваш файл jar Aspose.Cells Java в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\8. Клонировать примеры [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) внутри папки C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в папку с примерами Aspose.Cells Java for PHP.

\10. Перезапустите службу apache tomcat и начните использовать примеры. 
