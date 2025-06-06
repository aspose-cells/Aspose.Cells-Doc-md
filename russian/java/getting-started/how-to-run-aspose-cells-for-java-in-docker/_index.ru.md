---
title: Как запустить Aspose.Cells for Java в Docker
type: docs
description: "Запустить Aspose.Cells for Java в контейнере Docker для Linux."
weight: 139
url: /ru/java/how-to-run-aspose-cells-in-docker/
---

Микросервисы, в сочетании с контейнеризацией, позволяют легко объединять технологии. Docker позволяет легко интегрировать функциональность Aspose.Cells в ваше приложение, независимо от используемой технологии в вашем стеке разработки.

В случае, если вы используете микросервисы, или если основной технологией в вашем стеке не является .NET, C++ или Java, но вам нужна функциональность Aspose.Cells, или если вы уже используете Docker в своем стеке, вас может заинтересовать использование Aspose.Cells for Java в контейнере Docker.

## Предварительные требования

- Должен быть установлен Docker на вашей системе. 

## Создание приложения на Java

В этом примере вы создаете приложение на Java, которое создает простой файл xlsx, сохраняет его и читает. Приложение затем может быть собрано и запущено в Docker.

### Создание приложения на Java

Создайте приложение на Java в Eclipse, используя следующий код. В этом примере мы используем Aspose.Cells for Java для создания нового листа xlsx и устанавливаем его имя и значения ячейки, затем считываем и выводим их.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Создание приложения на Java в jar-пакет

На следующей картинке показан способ создания jar-пакета с помощью меню "Экспорт" в Eclipse.

**![Создание Jar с помощью Eclipse](MakeJar.png)**

Теперь, когда мы написали программу на Java, используя Aspose.Cells for Java, у нас есть jar-пакет. Далее мы создадим dockerfile.

### Настройка Dockerfile

Следующим шагом является создание и настройка Dockerfile.

1. Создайте dockerfile и поместите его рядом с jar-пакетом. Оставьте это имя файла без расширения (по умолчанию).
2. Укажите в dockerfile:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Сборка и запуск приложения в Docker

Теперь приложение можно собирать и запускать в Docker. Откройте ваш любимый командный интерпретатор, перейдите в каталог с Dockerfile и выполните следующую команду:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

После выполнения вышеуказанной команды вы получите вывод электронной таблицы формата XLSX и результат выполнения командной строки. На этом этапе программа на Java успешно запущена в Linux Docker.
{{< app/cells/assistant language="java" >}}
