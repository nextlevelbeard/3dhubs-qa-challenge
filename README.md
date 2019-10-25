## 3D Hubs QA challenge

#### Metrics

Initial call describing challenge on 22/10/2019 ~ 3PM

Proposed by email on 23/10/2019 ~ 11AM

Submission on 25/10/2019 ~ 9AM

*No previous knowledge of Python*

#### Bootstrapping

- Get Python 3.*
- Get `pipenv `
  - `pip install pipenv`
-  `cd` to the root of the project and run 
  - `pipenv install`
- Run (all) the tests
  - `pipenv run tests`

- Run BDD style tests: 
  - `pipenv run testsbdd`

#### Things to not miss about my application:

- Stack: *pytest, pytest-bdd, selenium 4*
- 4 tests total: 2 tests with *pytest* and 2 Scenarios with *pytest-bdd*🥒
  - *Can proceed to checkout after uploading a 3D model file*
  - *Can proceed to checkout by using the sample*

- Using Page Object model throughout
- Pipfile scripts 
- Gherkin Scenarios run from Home Page and on any viewport/device
- Implemented HTML report for the test runs
  - You should have a `report.html` in the root directory after running the tests
  - In the fat chance the tests fail a screenshot will be saved to the `assets` folder and attached to the report
- Found out where you keep your precious sample 3D model file you use for the sample demonstration and I used for the tests 😎
- Found some cool [issues](./issues)



#### Lessons learned

Read headaches.

On Python:

- Test definitions HAVE to start with 'test' 🙄
- The test setup file HAS to be named conftest.py 🙄
- Every folder/module NEEDS to be have a init.py in there for module resolution 🙄
  
  - The stable Python Selenium libraries are outdated as heck 🙄
  
  - they are non-W3C compliant, had to use an alpha version of the package
- The Python Selenium bindings REALLY wants the *chromedriver/geckodriver* file in the Windows' PATH  to have the .exe extension
  
  - could not use my already installed nodeJS drivers 😢🙄
- ...and many more to count/remember

Things I could improve, given more time: 

- Folder structure, file organization
- Parameterizing the BDD Scenarios for stuff like email