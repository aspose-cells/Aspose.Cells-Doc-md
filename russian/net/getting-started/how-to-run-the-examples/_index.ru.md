---
title: Как запустить примеры
type: docs
weight: 140
url: /ru/net/how-to-run-the-examples/
---

## **Требования к программному обеспечению**
Пожалуйста, убедитесь, что вы соответствуете следующим требованиям, прежде чем загружать и запускать примеры.

1. Visual Studio 2015 или выше
1. Установлен менеджер пакетов NuGet в Visual Studio. Он обычно уже установлен в Visual Studio 2015. Для получения подробной информации о том, как установить менеджер пакетов NuGet, пожалуйста, проверьте: [Установка инструментов клиента NuGet](https://docs.microsoft.com/ru-ru/nuget/install-nuget-client-tools)
1. Перейдите в раздел Tools->Options->NuGet Package Manager->Package Sources и убедитесь, что включена опция **nuget.org**
1. Пример проекта использует функцию автоматического восстановления пакета NuGet, поэтому должно быть активное интернет-соединение. Если у вас нет интернет-соединения на компьютере, на котором должны выполняться примеры, пожалуйста, проверьте [Установка и развёртывание](/cells/ru/net/installation-and-deployment/) и добавьте ссылку на Aspose.Cells.dll в проект примера вручную.
## **Скачать с GitHub**
Все примеры Aspose.Cells for .NET размещены на [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Примеры Aspose.Cells**
- Вы можете либо клонировать репозиторий с помощью вашего любимого клиента GitHub, либо скачать ZIP-файл с [здесь](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Извлеките содержимое ZIP-файла в любую папку на вашем компьютере. Все примеры находятся в папке **Examples**.
- Для примеров на C# имеется файл решения Visual Studio, т.е. **Aspose.Cells.Examples.CSharp.sln**.
- Проект создан и поддерживается в Visual Studio 2015.
- Откройте файл решения в Visual Studio и постройте проект.
- При первом запуске зависимости будут автоматически загружены через NuGet. Вы также можете скачать DLL-файлы отдельно с [здесь](https://downloads.aspose.com/cells/net).
- Папка **Data** в корневой папке **Examples** содержит входные файлы, используемые в примерах на C#. Необходимо загрузить папку **Data** вместе с проектом примеров.
- Откройте **RunExamples.cs**, все примеры вызываются отсюда.
- Разкомментируйте примеры, которые хотите запустить в рамках проекта.
## **Примеры Aspose.Cells.GridDesktop**
- Примеры Aspose.Cells.GridDesktop также включены в репозиторий [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) и будут доступны как часть ZIP-файла, доступного для скачивания [здесь](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Все примеры находятся в папке **Examples_GridDesktop**.
- Аналогично примерам Aspose.Cells, имя файла решения примеров GridWeb - **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Откройте файл решения в Visual Studio и постройте проект.
- Все зависимости включены в состав проекта примеров. Вы также можете скачать DLL-файлы отдельно с [здесь](https://downloads.aspose.com/cells/net).
- Папка **Data** в корневой папке **Examples_GridDesktop** содержит входные файлы, используемые примерами. Обязательно загрузите папку **Data** вместе с проектом примерами.
- Откройте и запустите проект.
- Нажмите на пример в меню, который вы хотите запустить из формы.
## **Примеры Aspose.Cells.GridWeb**
- Примеры Aspose.Cells.GridWeb также включены в репозиторий [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) и будут доступны в виде ZIP-файла, загружаемого отсюда [здесь](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Все примеры находятся в папке **Examples_GridWeb**.
- Аналогично примерам Aspose.Cells, имя файла решения примеров GridWeb - **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Откройте файл решения в Visual Studio и постройте проект.
- Все зависимости включены в проекты примеров. Вы также можете загрузить DLL-файлы отдельно отсюда [здесь](https://downloads.aspose.com/cells/net).
- Папка **Data** в корневой папке **Examples_GridWeb** содержит входные файлы, используемые примерами. Обязательно загрузите папку **Data** вместе с проектом примерами.
- Откройте и запустите **Examples.aspx** в проекте примеров.
- Нажмите на пример в браузере, который вы хотите запустить из проекта.
{{< app/cells/assistant language="csharp" >}}
