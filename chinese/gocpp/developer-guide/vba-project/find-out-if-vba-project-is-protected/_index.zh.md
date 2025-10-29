---  
title: 查明VBA项目是否被Golang via C++保护  
linktitle: 查看 VBA 项目是否已受保护  
type: docs  
weight: 20  
url: /zh/go-cpp/find-out-if-vba-project-is-protected/  
description: 使用Aspose.Cells与Golang via C++检测Excel文件中VBA项目是否受保护  
---  

## **用C++检测VBA项目是否受保护**

你可以使用[**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/)属性，判断Excel文件中的VBA（Visual Basic for Applications）项目是否被保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检测其VBA项目是否受保护，然后保护此VBA项目，再次检测。请查看控制台输出作为参考。在保护前，[**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/)返回**false**，保护后返回**true**。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
