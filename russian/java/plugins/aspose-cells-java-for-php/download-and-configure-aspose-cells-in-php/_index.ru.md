---
title: Загрузите и настройте Aspose.Cells в PHP
type: docs
weight: 10
url: /ru/java/download-and-configure-aspose-cells-in-php/
---
## **Скачать необходимые библиотеки**
Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения примеров Aspose.Cells Java for PHP.

- **Aspose:** [Aspose.Cells for Java Компонент](https://downloads.aspose.com/cells/java/)
- [PHP/Java Мост](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Загрузите примеры с сайтов социального кодирования**
Следующие выпуски работающих примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

-----
### **Гитхаб**
- **Aspose.Cells Java for PHP Примеры** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Как настроить исходный код на платформе Linux**
Пожалуйста, следуйте этим простым шагам, чтобы открыть и расширить исходный код при использовании:
## **1. Установите сервер Tomcat**
 Чтобы установить сервер Tomcat, введите следующую команду в консоли Linux. Это позволит успешно установить сервер tomcat.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Загрузите и настройте PHP/JavaBridge**
 Чтобы загрузить двоичные файлы PHP/JavaBridge, введите следующую команду в консоли Linux.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Разархивируйте двоичные файлы PHP/JavaBridge, выполнив следующую команду в консоли Linux.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Это позволит извлечь**JavaBridge.war**файл. Скопируйте его на tomcat88**веб-приложения** папку, выполнив следующую команду в консоли Linux.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


При копировании tomcat8 автоматически создаст новую папку "**JavaBridge**" в**веб-приложения**. После создания папки убедитесь, что ваш tomcat8 запущен, а затем проверьте<http://localhost:8080/JavaBridge> в браузере должна открыться страница JavaBridge по умолчанию.

 Если появится какое-либо сообщение об ошибке, установите**FastCGI**введя следующую команду в консоли Linux.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

После установки php5.5 cgi перезапустите сервер tomcat8 и проверьте<http://localhost:8080/JavaBridge>снова в браузере.

Если**JAVA_HOME**отображается ошибка, затем откройте файл /etc/default/tomcat8 и раскомментируйте строку, которая устанавливает JAVA_HOME. Снова проверьте <http://localhost:8080/JavaBridge> в браузере, он должен появиться на странице примеров PHP/JavaBridge.
## **3. Настройте Aspose.Cells Java for PHP Примеры**
 Клонируйте примеры PHP, выполнив следующие команды в папке webapps/JavaBridge.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Как настроить исходный код на платформе Windows**
Пожалуйста, выполните следующие простые шаги для настройки моста PHP/Java на платформе Windows.

\1. Установите PHP5 и настройте как обычно
\2. Установите JRE 6 (Java Runtime Environment), если она еще не установлена. Вы можете проверить это в C:\Program Files и т. д. Вы можете скачать его здесь. Я использую JRE 6, поскольку он совместим с мостом PHP Java (PJB).

\3. Установите Apache Tomcat 8.0. Вы можете скачать это здесь

 4.Скачать[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Скопируйте этот файл в каталог веб-приложений tomcat.
(например: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

\5. Перезапустите службу Apache Tomcat.

 6.Перейти к<http://localhost:8080/JavaBridge/test.php> чтобы проверить, работает ли php. Вы можете найти другие примеры там

7. Скопируйте файл jar Aspose.Cells Java в папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

 \8. Клон[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) примеры внутри папки C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в папку с примерами Aspose.Cells Java for PHP.

 \10. Перезапустите службу Apache Tomcat и начните использовать примеры.
