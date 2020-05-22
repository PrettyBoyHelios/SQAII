# Test Plan for Android Testing Suite
May 20th, 2020  
SDET: *Luis Enrique Correa Morán*

## Table of Contents
1. [Project Definition](#10-project-definition)
2. [Scope](#20-scope)
3. [Testing Levels](#30-testing-levels)
4. [Test Strategy](#40-test-strategy)
5. [Exit Criteria](#50-exit-criteria)
6. [Risk Analysis](#60-risk-analysis)
7. [Project Planning](#70-project-planning)

## 1.0 Project Definition
Android Testing Suite is a Software Development that aims to create an in-house testing suite for some of Android's most important modules.
The testing suite is expected to guarantee the correct app behaviour for the Phone, Calculator and Settings apps. It is expected for the framework to be highly optimized, flexible and scalable to accommodate for a variety of different modules (or Apps) in the future.

## 2.0 Scope
The project will cover the following areas for the described three modules of the Android ecosystem.

* Phone App  
    * Ability of performing local calls.  
    * Ability to make international calls.  
    * Ability to reach emergency numbers.  
* Calculator  
    * Correct handling of the sum, division, subtraction and multiplication operations.  
    * Correct handling of complex operations.  
    * Handling of edge cases with arithmetic errors and exceptions.  
    
* WiFi Settings  
    * Ability to perform state changes on the WiFi connectivity for a device.  

### 2.1 Out of Scope
Any interaction of the aforementioned apps with external apps or devices will be left out of the testing scope. All tests must be run in app and on device.  
Also, it is important to mention that the testing suite will only cover the development of the core Android Apps in 
their 'Vanilla' version, what's often described as Pure Android versions of the apps, as OEM personalization layers may introduce screen elements that may be too 
much to generalize and create an optimized framework.

## 3.0 Testing Levels
This project will focus black box testing, evaluating only the outcome of a given process. The testing suite will provide both **system** and **regression** testing to the Android core app development. As the testing framework will provide a comprehensive way of testing the work of all the components of an app, and to guarantee the app's behaviour on every release.  

## 4.0 Test Strategy
The testing developed for this project will consist mainly on System Testing as well as Integration Testing, it is expected from the developers of Android Apps to perform the relevant Unit Testing before pushing new builds for testing.

At the same time, the following roles have been identified to be required for the project.  
| Role           | Responsibilities                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SDET           | Review test documentation, and verify all of the testing activities performed help towards the testing objectives of the project.                                                                                        |
| Tester         | To execute the tools created for the project, to make software evaluation and reports.                                                                                                                                   |
| Lead Developer | To coordinate all development activities, and organizing all of them so that schedules are met. Review architectural design for the testing tools and prepare all needed environments for the Testing Suite to run over. |
| Developers     | To develop the required tools and processes for testing throughout the project. All of this must be documented.                                                                                                          |

### 4.1 Test Environment
For the testing environment an inhouse server(s) is recommended, as physical access to devices is required. The hardware required is specified below.
* An Intel-based system is required as AMD's recent Ryzen Platform has some issues with the libraries used for the project.
* A Linux (Preferably Linux or Debian) or macOS system (a UNIX system) is recommended over a Windows server.
* A machine with at least 8GM of RAM is recommended
* Intel's 8th GEN or later processors recommended.
* USB Extending devices, to maximize the amount of devices on each run.

## 5.0 Exit Criteria
For a release to be approved and deployed, the following conditions must be met.  
* The targeted version must pass 97% of the planned test cases.
* All bugs in the released have been identified, analyzed and documented.
* The Project's Lead Developer & Tester have agreed the found bugs do not represent a risk for the platforms overall functionality or credibility.
* All changes have been documented and all reasonable Test Suites have been run to validate the current build.
* Installation of Python 2.7 and virtualenv, as well as all the dependencies established in requirements.txt.

### 5.1 For the Client Devices
* English versions of the OS Installed.
* Pure Android versions of Android (7.0-10.0).
* Debugging over USB Activated & with screen power off disabled.
* Settings, Calculator and Phone apps on the main device screen.

## 6.0 Risk Analysis
The following risks and their respective mitigation strategies have been identified as likely hazards to the project.

| Risk                                                                                                           | Likelihood | Impact | Mitigation                                                                                         |
|----------------------------------------------------------------------------------------------------------------|------------|--------|----------------------------------------------------------------------------------------------------|
| Reduced Personal for the Project                                                                               | 5          | 4      | Set realistic feature sets & times for product release.                                            |
| Limited knowledge & proficiency on the tools chosen for the project                                            | 5          | 2      | Rely on more experienced members of the group that may be able of helping.                         |
| SARS-COVID19 Pandemic                                                                                          | 5          | 1      | Replace communication methods for videoconferencing for meetings and advisory.                     |
| Android Fragmentation causes for an unmanageable number of devices/ versions of the app to be tested properly. | 5          | 3      | Narrow down the Android versions & variants to create a Highly optimized version of the framework. |
| Loss of Projects Documentation                                                                                 | 3          | 4      | Create automated reports of the testing and properly label every version of all documents.         |

## 7.0 Project Planning

### 7.1 Project Deliveries
| Activity  | Delivery Date | Start Date |
|-----------|---------------|------------|
| v1.0      | 30/03/2020    | 18/04/2020 |
| v1.1      | 04/05/2020    | 11/05/2020 |
| v1.2      | 11/05/2020    | 22/05/2020 |
| Live Demo | 22/05/2020    | 23/05/2020 |

### 7.2 Project Roles
| Role                      | Assignee                  |
|---------------------------|---------------------------|
| Product Owner             | Juan de Dios Delgado      |
| SDET                      | Luis Enrique Correa Morán |
| Developer, LEAD Developer | Luis Enrique Correa Morán |
| Tester                    | Luis Enrique Correa Morán |
