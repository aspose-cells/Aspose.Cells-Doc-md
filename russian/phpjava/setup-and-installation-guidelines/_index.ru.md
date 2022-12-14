---
title: Руководство по настройке и установке
type: docs
weight: 20
url: /ru/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: настроить Aspose.Cells для PHP через Java и руководство по установке
---
## **Системные Требования**
Aspose.Cells для PHP через Java не зависит от платформы API и может использоваться на любой платформе (Windows, Linux, MacOS и т. д.), где[PHP](https://www.php.net/downloads.php)Установлена 7 или более поздняя версия. Перед настройкой установки на компьютере должна быть установлена версия Oracle JDK 7 или выше.
## **Установка и использование**
Aspose.Cells для PHP через Java распространяется в виде ZIP-архива.

Чтобы настроить среду, установите и используйте Aspose.Cells для PHP через Java, следуйте инструкциям:
### **Линукс:**
- Скачать[PHP](https://www.php.net/downloads.php)источник и установить его. Или используйте команду «sudo apt install php-xxx» для установки двоичного файла php.
- Установите Oracle JDK (1.7 или 1.8) для Linux, настройте переменную среды JAVA_HOME.
- Загрузите/получите «Aspose.Cells для PHP через Java» API и извлеките его. Там будет папка с именем «aspose.cells».
- Загрузите двоичный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папке «aspose.cells».
- Загрузите библиотеку PHP java/Java.inc (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните ее в папке «aspose.cells».
- Запустите «PHP/Java Bridge» в указанной выше папке с помощью приведенной ниже команды.

|$JAVA_ГЛАВНАЯ/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar СЕРВЛЕТ_МЕСТНО:8080 >/dev/null 2>&1 &|
|:- |
- Запустите «example.php» в папке «aspose.cells», чтобы запустить пример с помощью следующей команды:

|$php пример.php|
|:- |
### **Windows:**
- Скачать[PHP](https://www.php.net/downloads.php)двоичный файл Windows и добавьте «php.exe» в PATH.
- Установите Oracle JDK (1.7 или 1.8) для Windows и настройте переменную среды JAVA_HOME.
- Загрузите «Aspose.Cells для PHP через Java» API и распакуйте его. Там будет папка с именем «aspose.cells».
- Загрузите двоичный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папке «aspose.cells».
- Загрузите библиотеку PHP java/Java.inc (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните ее в папке «aspose.cells».
- Запустите «PHP/Java Bridge» в указанной выше папке с помощью приведенной ниже команды. Выберите порт прослушивателя http 8080 при запуске моста и нажмите кнопку OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Запустите «example.php» в папке «aspose.cells», чтобы запустить пример с помощью следующей команды:

|> пример php.php|
|:- |
### **Мак:**
- Установить[PHP](https://www.php.net/downloads.php).
- Установите Oracle JDK (1.7 или 1.8) для Mac, настройте переменную среды JAVA_HOME.
- Загрузите «Aspose.Cells для PHP через Java» API и распакуйте его. Там будет папка с именем «aspose.cells».
- Загрузите двоичный файл PHP/Java Bridge (JavaBridge.jar) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните его в папке «aspose.cells».
- Загрузите библиотеку PHP java/Java.inc (Java.inc) с http://php-java-bridge.sourceforge.net/pjb/download.php и сохраните ее в папке «aspose.cells».
- Запустите «PHP/Java Bridge» в указанной выше папке с помощью приведенной ниже команды. Выберите порт прослушивателя http 8080 при запуске моста и нажмите кнопку OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Запустите «example.php» в папке «aspose.cells», чтобы запустить пример с помощью следующей команды:

|$php пример.php|
|:- |


