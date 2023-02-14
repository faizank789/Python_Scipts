def processBuilder = new ProcessBuilder('/bin/bash', '-c', '/path/to/script.sh')
def process = processBuilder.start()
process.waitFor()

if (process.exitValue() == 0) {
    println 'Script executed successfully'
} else {
    println "Script failed with exit code ${process.exitValue()}"
}
