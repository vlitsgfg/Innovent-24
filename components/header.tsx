export default function Header() {
  return (
    <header className="h-full bg-zinc-800 py-4">
      <div className="flex items-center justify-between mx-auto max-w-[1000px]">
        <div className="cursor-pointer">LOGO</div>
        <div className="text-3xl">CodeGPT</div>
        <div className="flex items-center gap-4">
          <div className="bg-zinc-900 hover:bg-white px-4  hover:text-black rounded-lg py-2 cursor-pointer">
            Login
          </div>
          <div className="bg-zinc-900 hover:bg-white px-4  hover:text-black rounded-lg py-2 cursor-pointer">
            Signup
          </div>
        </div>
      </div>
    </header>
  );
}
