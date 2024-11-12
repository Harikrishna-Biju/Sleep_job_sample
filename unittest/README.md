go test -json -v -cover ./... > test/unittest/testresults.json

go test -v -coverprofile=coverage ./... | tee test/unittest/coverage.out

go install github.com/jstemmer/go-junit-report/v2@latest
cat test/unittest/coverage.out | go-junit-report > test/unittest/covreport.xml

go install github.com/axw/gocov/gocov@latest
go install github.com/AlekSi/gocov-xml@latest
gocov convert test/unittest/coverage.out | gocov-xml > test/unittest/codecoverage.xml