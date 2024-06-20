---
title: Начало работы
type: docs
weight: 10
url: /ru/cpp/getting-started/
description: Как установить Aspose Cells для C++ и создать простое приложение Hello World.
---

{{% alert color="primary" %}} 

На этой странице будет показано, как установить Aspose Cells для C++ и создать простое приложение Hello World.

{{% /alert %}}

## **Установка**

### **Установите Aspose Cells через NuGet**

NuGet - самый простой способ загрузки и установки Aspose.Cells for C++. 
1. Создайте проект Microsoft Visual Studio для C++.
2. Включите заголовочный файл "Aspose.Cells.h".
3. Откройте Microsoft Visual Studio и менеджер пакетов NuGet.
4. Поиск "aspose.cells.cpp", чтобы найти нужный Aspose.Cells for C++. 
5. Щелкните "Установить", Aspose.Cells for C++ будет загружен и добавлен в ваш проект.

**![Установка Aspose Cells через NuGet](InstallThroughNuget.png)**

Вы также можете загрузить его со страницы NuGet для aspose.cells: 
[Пакет NuGet Aspose.Cells for C++](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Больше деталей пошагово](/cells/ru/cpp/installation/)

### **Демонстрация использования Aspose.Cells for C++ в Windows**

1. Скачайте Aspose.Cells for C++ с следующей страницы:
[Загрузить Aspose.Cells for C++ (для Windows)](https://downloads.aspose.com/cells/cpp/)
2. Распакуйте пакет, и вы найдете пример использования Aspose.Cells for C++.
3. Откройте пример.sln в Visual Studio 2017 или более новой версии
4. main.cpp: этот файл показывает, как написать код для тестирования Aspose.Cells for C++.

### **Демонстрационный пример использования Aspose.Cells for C++ в Linux.**

1. Скачайте Aspose.Cells for C++ с следующей страницы:
[Загрузить Aspose.Cells for C++ (для Linux)](https://downloads.aspose.com/cells/cpp/)
2. Распакуйте пакет, и вы найдете пример использования Aspose.Cells for C++ для Linux.
3. Убедитесь, что вы находитесь в папке, где находится пример.
4. Запустите "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Запустите "cmake --build example/build"

### **Демонстрационный пример использования Aspose.Cells for C++ в Mac OS.**

1. Скачайте Aspose.Cells for C++ с следующей страницы:
[Загрузить Aspose.Cells for C++ (для MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Распакуйте пакет, и вы найдете пример использования Aspose.Cells for C++ для MacOS.
3. Убедитесь, что вы находитесь в папке, где находится пример.
4. Запустите "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Запустите "cmake --build example/build"

## **Создание приложения Hello World**

Нижеприведенные шаги создают приложение Hello World с использованием API Aspose.Cells:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Если у вас есть лицензия, тогда [примените ее](/cells/ru/cpp/licensing/).
   Если вы используете пробную версию, пропустите строки кода, связанные с лицензией.
1. Получите доступ к любой желаемой ячейке листа Excel в файле Excel.
1. Вставьте слова "**Привет, мир!**" в доступную ячейку.
1. Сгенерируйте модифицированный файл Microsoft Excel.

Реализация вышеуказанных шагов продемонстрирована в примерах ниже.

### **Пример кода: Создание новой книги**

В следующем примере создается новая книга с нуля, вставляется "**Привет, мир!**" в ячейку A1 на первом листе и сохраняется файл Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Пример кода: Открытие существующего файла**

В следующем примере открывается существующий шаблон Microsoft Excel, получается ячейка и проверяется значение в ячейке A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
