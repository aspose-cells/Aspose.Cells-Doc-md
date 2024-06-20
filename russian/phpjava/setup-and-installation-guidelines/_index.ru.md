---
title: Руководство по установке и настройке
type: docs
weight: 20
url: /ru/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "настройка Aspose.Cells для PHP via Java и руководство по установке."
---



## **Системные требования**
Aspose.Cells для PHP via Java является платформенно-независимым API и может быть использован на любой платформе (Windows, Linux, MacOS и т.д.), где установлены версии PHP 7 или выше. На машине должен быть установлен Oracle JDK 7 или более поздние версии перед установкой.
## **Установка и использование**
Aspose.Cells для PHP via Java распространяется в виде ZIP-архива.

Чтобы настроить среду, установить и использовать Aspose.Cells для PHP via Java, следуйте инструкциям:
### **Linux:**
- Загрузите [PHP](https://www.php.net/downloads.php) исходный код и установите его. Или используйте команду "sudo apt install php-xxx" для установки бинарного файла php.
- Установите Oracle JDK (1.7 или 1.8) для Linux, настройте переменную среды JAVA_HOME.
- Скачайте/получите API "Aspose.Cells для PHP via Java" и извлеките его. Там будет папка с названием "aspose.cells".
- Скачайте бинарный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папку "aspose.cells".
- Скачайте библиотеку java/Java.inc PHP (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните её в папку "aspose.cells".
- Запустите "PHP/Java Bridge" в указанной выше папке с помощью следующей команды.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Запустите "example.php" в папке “aspose.cells” с помощью следующей команды:

|$ php example.php|
| :- |
### **Windows:**
- Скачайте [PHP](https://www.php.net/downloads.php) бинарный файл для Windows и добавьте "php.exe" в PATH.
- Установите Oracle JDK (1.7 или 1.8) для Windows и настройте переменную среды JAVA_HOME.
- Скачайте API "Aspose.Cells для PHP via Java" и извлеките её. Там будет папка с именем "aspose.cells".
- Скачайте бинарный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папку "aspose.cells".
- Скачайте библиотеку java/Java.inc PHP (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните её в папку "aspose.cells".
- Запустите “PHP/Java Bridge” в указанной выше папке с помощью следующей команды. При запуске моста выберите порт прослушивания 8080 http и нажмите кнопку OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Запустите "example.php" в папке “aspose.cells” с помощью следующей команды:

|> php example.php|
| :- |
### **Mac:**
- Установите [PHP](https://www.php.net/downloads.php).
- Установите Oracle JDK (1.7 или 1.8) для Mac, настройте переменную среды JAVA_HOME.
- Скачайте API "Aspose.Cells для PHP via Java" и извлеките её. Там будет папка с именем "aspose.cells".
- Скачайте бинарный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папку "aspose.cells".
- Скачайте библиотеку java/Java.inc PHP (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните её в папку "aspose.cells".
- Запустите “PHP/Java Bridge” в указанной выше папке с помощью следующей команды. При запуске моста выберите порт прослушивания 8080 http и нажмите кнопку OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Запустите "example.php" в папке “aspose.cells” с помощью следующей команды:

|$ php example.php|
| :- |


