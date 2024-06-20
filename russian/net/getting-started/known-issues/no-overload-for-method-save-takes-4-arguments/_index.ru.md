---
title: Нет перегрузки метода Save, принимающего 4 аргумента
type: docs
weight: 70
url: /ru/net/no-overload-for-method-save-takes-4-arguments/
---

## **Симптом**

"Используя версию Aspose.Cells, я получаю эту ошибку, когда использую метод Save при попытке сохранить книгу в объект Response. Я нашел этот фрагмент кода в онлайн-документации."

### **Снимок экрана ошибки**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **Решение**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET совместим и работает отлично со всеми версиями .NET Framework, т.е. 2.x, 3.x, 4.x и т.д. для любого типа проекта, например Asp.NET/Winforms, веб-проект, Windows/Web-служба, консольное приложение или другие проекты и т.д. Мы предоставляем разные dll-файлы для разных версий .NET Framework. Для получения дополнительной информации ознакомьтесь с файлом **readme.txt** в папке "\Bin" по адресу вашего установочного каталога. Однако этот **readme.txt** файл присутствует.

Когда вы используете наш продукт в веб-приложении, пожалуйста, используйте Aspose.Cells.dll из папки **NET 2.0** в каталоге "/bin". Для вашей информации, dll в папке **.NET 3.5 Client Profile** используется только для консольного приложения с профилем клиентского фреймворка Net в качестве целевого фреймворка VS.NET. Проверьте свой проект, возможно, ваш проект ссылается на этот dll.

### **Ссылки**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
