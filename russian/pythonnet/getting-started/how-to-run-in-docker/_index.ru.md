---
title: Как запустить Aspose.Cells для python via .NET в Docker
type: docs
description: Запустите Aspose.Cells в контейнере Docker для Linux
weight: 140
url: /ru/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Предисловие:

Всё больше пользователей используют различные продукты нашей компании в Docker и сталкиваются с различными проблемами. В этой статье кратко описано, как использовать Aspose.Cells для Python via .NET в среде Docker на основе Debian Linux.

## Пример:

Мы иллюстрируем использование простым примером. В этом случае функциональность очень простая, просто открываем файл Excel, содержащий японский текст, в aspose_test.py. Здесь мы используем python:3.11 в качестве базового образа, и соответствующий Dockerfile выглядит следующим образом:

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

Затем, запустив следующую команду, мы получаем окончательный результат:
- Собрать образ Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Запустить образ Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Примечание:

Чтобы поддерживать открытие файлов Excel, содержащих различные языки, нам нужно установить ICU. Учитывая, что оболочка Python via .NET основана на .NET Core 3.1, у которого есть специфические требования к версии ICU, не превышающие версии 70, нам нужно установить конкретную версию ICU.


## См. также

- [Установите Docker Desktop на Windows](https://docs.docker.com/docker-for-windows/install/)
