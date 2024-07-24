---
title: How to Run Aspose.Cells for python via .NET in Docker
type: docs
description: "Run Aspose.Cells in a Docker container for Linux"
weight: 140
url: /net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Preface；

More and more users are using our company's various products in Docker, and they encounter various issues. This article briefly introduces how to use Aspose.Cells for Python via .NET in a Docker environment based on Debian Linux.

## Example；

We illustrate the usage with a simple example. In this case, the functionality is very straightforward, just opening an Excel file containing Japanese text in aspose_test.py. Here, we use python:3.11 as the base image, and the corresponding Dockerfile is as follows:

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

Then, when we run the following command, we obtain the final result:
- Build Docker Image

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Run Docker Image

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Note:

To support opening Excel files containing various languages, we need to install ICU. Considering that the Python via .NET wrapper is based on .NET Core 3.1, and .NET Core 3.1 has specific version requirements for ICU, which should not exceed version 70, we need to install a specific version of ICU.


## See Also

- [Install Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/)
