def dir = new File('/path/to/existing/directory')
if (dir.exists() && dir.isDirectory()) {
    println 'Directory exists'
} else {
    println 'Directory does not exist'
}
