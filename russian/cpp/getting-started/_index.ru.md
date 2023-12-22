---
title: Начиная
type: docs
weight: 10
url: /ru/cpp/getting-started/
description: Как установить Aspose Cells for C++ и создать приложение Hello World.
---
{{% alert color="primary" %}} 

На этой странице показано, как установить Aspose Cells for C++ и создать приложение Hello World.

{{% /alert %}}

##  **Монтаж**

###  **Установите номера с Aspose по Cells–NuGet.**

 NuGet — это самый простой способ загрузить и установить Aspose.Cells for C++.
1. Создайте проект Visual Studio Microsoft for C++.
2. Включите файл заголовка «Aspose.Cells.h».
3. Откройте Microsoft Visual Studio и менеджер пакетов NuGet.
 4. Выполните поиск «aspose.cells.cpp», чтобы найти нужный Aspose.Cells for C++.
5. Нажмите «Установить», Aspose.Cells for C++ будет загружен и использован в вашем проекте.

**![Установите Aspose Cells–NuGet](InstallThroughNuget.png)**

 Вы также можете загрузить его с веб-страницы nuget aspose.cells:
[Aspose.Cells for C++ NuGet Пакет](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Дополнительный шаг для получения подробной информации](/cells/ru/cpp/installation/)

###  **Демо-версия использования Aspose.Cells for C++ на Windows.**

1. Загрузите Aspose.Cells for C++ со следующей страницы:
[Скачать Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Разархивируйте пакет, и вы найдете пример использования Aspose.Cells for C++.
3. Откройте файл example.sln в Visual Studio 2017 или более поздней версии.
4. main.cpp: в этом файле показано, как написать код для проверки Aspose.Cells for C++

###  **Демо-версия использования Aspose.Cells for C++ в Linux.**

1. Загрузите Aspose.Cells for C++ со следующей страницы:
[Скачать Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Разархивируйте пакет, и вы найдете пример использования Aspose.Cells for C++ для Linux.
3. Убедитесь, что вы находитесь по пути, по которому находится пример.
4. Запустите «cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release».
5. Запустите «cmake --build example/build».

###  **Демо-версия использования Aspose.Cells for C++ в Mac OS.**

1. Загрузите Aspose.Cells for C++ со следующей страницы:
[Скачать Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Разархивируйте пакет, и вы найдете пример использования Aspose.Cells for C++ для MacOS.
3. Убедитесь, что вы находитесь по пути, по которому находится пример.
4. Запустите «cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release».
5. Запустите «cmake --build example/build».

##  **Создание заявления Hello World**

Следующие шаги создают приложение Hello World с использованием Aspose.Cells API:

1.  Создайте экземпляр[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) сорт.
1.  Если у вас есть лицензия, то[применить это](/cells/ru/cpp/licensing/).
 Если вы используете ознакомительную версию, пропустите строки кода, связанные с лицензией.
1. Получите доступ к любой желаемой ячейке листа в файле Excel.
1. Вставьте слова «**Hello World!**» в ячейку, к которой осуществляется доступ.
1. Создайте измененный файл Excel Microsoft.

Реализация вышеописанных шагов продемонстрирована на примерах ниже.

###  **Пример кода: создание новой книги**

В следующем примере создается новая книга с нуля, вставляется «**Hello World!**» в ячейку A1 на первом листе и сохраняется файл Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **Пример кода: открытие существующего файла**

В следующем примере открывается существующий файл шаблона Excel Microsoft, извлекается ячейка и проверяется значение в ячейке A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
