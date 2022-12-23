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

## **Установка**

### **Установите Aspose Cells до NuGet**

 NuGet — это самый простой способ загрузить и установить Aspose.Cells for C++.
1. Создайте проект Visual Studio Microsoft for C++.
2. Включить заголовочный файл "Aspose.Cells.h".
3. Откройте Microsoft Visual Studio и диспетчер пакетов NuGet.
4. Выполните поиск «aspose.cells.cpp», чтобы найти нужный Aspose.Cells for C++.
5. Нажмите «Установить», Aspose.Cells for C++ будет загружен и указан в вашем проекте.

**![Установить с Aspose Cells по NuGet](InstallThroughNuget.png)**

 Вы также можете загрузить его с веб-страницы nuget для aspose.cells:
[Aspose.Cells for C++ NuGet Пакет](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Больше шагов для деталей](/cells/ru/cpp/installation/)

### **Демо для использования Aspose.Cells for C++ на Windows**

1. Загрузите Aspose.Cells for C++ со следующей страницы:
[Скачать Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Разархивируйте пакет, и вы найдете демонстрацию о том, как использовать Aspose.Cells for C++.
3. Откройте Demo.sln в Visual Studio 2017 или более поздней версии.
4. main.cpp: этот файл показывает, как написать код для тестирования Aspose.Cells for C++
 5. sourceFile/resultFile: эти две папки являются каталогами хранения, используемыми в main.cpp.

### **Как использовать Aspose.Cells for C++ в ОС Linux**

1. Загрузите Aspose.Cells for C++ со следующей страницы:
[Скачать Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Разархивируйте пакет, и вы найдете демонстрацию о том, как использовать Aspose.Cells for C++ для Linux.
3. Запустите «cd Demo» в командной строке Linux.
4. Запустите "rm -rf build;mkdir build;cd build"
5. Запустите «cmake ..», чтобы создать Makefile с помощью CMakeLists.txt в папке Demo.
6. Запустите «make» для компиляции
 7. Запустите "./demo" вы увидите результат

## **Создание приложения Hello World**

Следующие шаги создают приложение Hello World, используя Aspose.Cells API:

1.  Создайте экземпляр[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) учебный класс.
1.  Если у вас есть лицензия, то[применить это](/cells/ru/cpp/licensing/).
 Если вы используете ознакомительную версию, пропустите строки кода, связанные с лицензией.
1. Получите доступ к любой нужной ячейке рабочего листа в файле Excel.
1. Вставьте слова «**Hello World!**" в ячейку, к которой осуществляется доступ.
1. Создайте измененный файл Excel Microsoft.

Реализация вышеуказанных шагов продемонстрирована на примерах ниже.

### **Пример кода: создание новой книги**

В следующем примере создается новая книга с нуля, вставляется "**Hello World!**" в ячейку A1 на первом листе и сохраняет файл Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Пример кода: открытие существующего файла**

В следующем примере открывается существующий файл шаблона Excel Microsoft, извлекается ячейка и проверяется значение в ячейке A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
